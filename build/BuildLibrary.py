import os
import stat
import shutil
import time
import sys
from multiprocessing import cpu_count

currentTime = time.localtime()
strTime = "%d-%02d-%02d %02d:%02d:%02d" % (currentTime.tm_year, currentTime.tm_mon, currentTime.tm_mday, currentTime.tm_hour, currentTime.tm_min,currentTime.tm_sec)

# 库名称
libraryName = "YOLOv3"

# git信息
gitBranch = "unknown"
gitCommitId = "unknown"

# 编译类型，编译debug版本还是release版本
compileType = "release"

# 编译器，支持g++和clang
compiler = "g++"

#------------------------函数的定义-------------------------#

#清理
def cleanFiles(path):
    if not os.path.exists(path):
        return

    shutil.rmtree(path)

#解析参数
def parseArgs():
    global compileType, compiler

    if "debug" in sys.argv:
        compileType = "debug"
    else:
        compileType = "release"

    if "clang++" in sys.argv:
        compiler = "clang++"
    else:
        compiler = "g++"

#获取git的信息（获取当前分支以及commit id）
def getGitInfo():
    global gitBranch, gitCommitId

    gitDir = "../.git"

    #获取分支信息
    branchFile = os.path.join(gitDir, "HEAD")
    if os.path.exists(branchFile):
        with open(branchFile, "r") as f:
            line = f.readline()
            line = line.strip()
            splits = line.split("/")
            if len(splits) > 0:
                gitBranch = splits[-1]

    # 获取commit id
    commitIdFile = os.path.join(gitDir + "/refs/heads", gitBranch)
    if os.path.exists(commitIdFile):
        with open(commitIdFile) as f:
            line = f.readline()
            line = line.strip()
            gitCommitId = line

#编译各个模块
def compileModules():
    global libraryName

    compileSuccessful = True

    # 创建软连接
    libraryPath = []
    for library in libraryPath:
        createSymbolLink(library)

    try:
        projectFile = "../" + libraryName + ".pro"
        if not os.path.exists(projectFile):
            print("not find project file %s"%projectFile)
            raise Exception("not find project file %s"%projectFile)

        with open(projectFile, "r") as file:
            for lineData in file:
                if lineData.find("./") <= 0:
                    continue

                lineData = lineData.replace("\\", "")
                lineData = lineData.strip()
                (path, file) = os.path.split(lineData)
                path = path.replace("./", "../src/")
                if not compileOneModule(path, file):
                    raise Exception("compile  module fail")

    except:
        compileSuccessful = False
    finally:
        # 删除软连接
        for library in libraryPath:
            removeSymbolLink(library)

    return compileSuccessful

#编译一个模块
def compileOneModule(modulePath, module):
    global gitBranch, gitCommitId, compileType, compiler

    print("\n------------compile module %s-------------"%(module))
    gitBranchMacro = "GIT_BRANCH=%s"%(gitBranch)
    gitCommitMacro = "GIT_COMMIT_ID=%s"%(gitCommitId)
    if not os.path.exists(modulePath):
        print("compile module fail, not find module directory, module path:%s, module name:%s"%(modulePath, module))
        return False

    moduleProFile = os.path.join(modulePath, module)
    if not os.path.exists(moduleProFile):
        print("compile module fail, not find pro file, module path:%s, module name:%s"%(modulePath, module))
        return False

    # 删除原来的makefile
    makefileName = os.path.join(modulePath, "Makefile")
    if os.path.exists(makefileName):
        os.remove(makefileName)

    # 生成新的makefile
    os.system("qmake DEFINES+=%s DEFINES+=%s QMAKE_CXX=%s QMAKE_LINK=%s CONFIG+=%s -o %s %s"%(gitBranchMacro, gitCommitMacro, compiler, compiler, compileType, makefileName, moduleProFile))
    if not os.path.exists(makefileName):
        print("qmake fail, module name:" + module + ", not find makefile")
        return False

    currentPath = os.getcwd()
    os.chdir(modulePath)
    os.system("make clean")
    if os.system("make -j %d "%cpu_count()) != 0:
        os.chdir(currentPath)
        print("---------compile module " + module + " fail, please check code---------")
        return False

    os.chdir(currentPath)
    return True

#创建符号链接
def createSymbolLink(path):
    if not os.path.exists(path):
        return

    files = os.listdir(path)
    for file in files:
        filename = os.path.join(path, file)
        if os.path.isdir(filename) or os.path.islink(filename) or filename.endswith(".so"):
            continue

        index = file.find(".so")
        if index <= 0:
            continue

        symbolName = file[:index + 3]
        if os.path.exists(os.path.join(path, symbolName)):
            continue

        currentPath = os.getcwd()
        os.chdir(path)
        os.symlink(file, symbolName)
        os.chdir(currentPath)

#删除符号链接
def removeSymbolLink(path):
    if not os.path.exists(path):
        return

    files = os.listdir(path)
    for file in files:
        if os.path.islink(os.path.join(path, file)):
            os.remove(os.path.join(path, file))

#构建服务
def buildService():
    outputDir = "./bin"
    parseArgs()
    cleanFiles(outputDir)
    getGitInfo()

    #编译各个模块
    if not compileModules():
        print("\n--------------compile fail at %s--------------" % (strTime))
        return -1

    print("\n--------------compile successful at %s--------------"%(strTime))
    return 0

#------------------------函数的调用-------------------------#
buildService()