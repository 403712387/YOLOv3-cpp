CONFIG -= app_bundle
CONFIG -= qt
CONFIG += c++11 console
TARGET = darknet
TEMPLATE = app
OBJECTS_DIR = ./output
MOC_DIR = ./output

INCLUDEPATH += \
    ./src \
    ./include

win32 {
DESTDIR = ./bin/windows
DEFINES += DARKNET_EXPORT=__declspec(dllimport)
LIBS += -L./bin -ldarknet \
    -lWs2_32 -lMswsock
}

unix {
DESTDIR = ./bin/linux
DEFINES += DARKNET_EXPORT=
LIBS += -L./bin -ldarknet
}

HEADERS += \
    include/darknet.h

SOURCES += \
    examples/art.cpp \
    examples/attention.cpp \
    examples/captcha.cpp \
    examples/cifar.cpp \
    examples/classifier.cpp \
    examples/coco.cpp \
    examples/darknet.cpp \
    examples/detector.cpp \
    examples/dice.cpp \
    examples/go.cpp \
    examples/instance-segmenter.cpp \
    examples/lsd.cpp \
    examples/nightmare.cpp \
    examples/regressor.cpp \
    examples/rnn.cpp \
    examples/rnn_vid.cpp \
    examples/segmenter.cpp \
    examples/super.cpp \
    examples/swag.cpp \
    examples/tag.cpp \
    examples/voxel.cpp \
    examples/writing.cpp \
    examples/yolo.cpp
