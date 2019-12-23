CONFIG -= app_bundle
CONFIG -= qt
CONFIG += c++11 console
TARGET = darknet
TEMPLATE = lib
DESTDIR = ./bin
OBJECTS_DIR = ./output
MOC_DIR = ./output

INCLUDEPATH += \
    ./src \
    ./include

win32 {
DEFINES += DARKNET_EXPORT=__declspec(dllexport)
}

unix {
DEFINES += DARKNET_EXPORT=
}

HEADERS += \
    include/darknet.h \
    src/activation_layer.h \
    src/activations.h \
    src/avgpool_layer.h \
    src/batchnorm_layer.h \
    src/blas.h \
    src/box.h \
    src/classifier.h \
    src/col2im.h \
    src/connected_layer.h \
    src/convolutional_layer.h \
    src/cost_layer.h \
    src/crnn_layer.h \
    src/crop_layer.h \
    src/cuda.h \
    src/data.h \
    src/deconvolutional_layer.h \
    src/demo.h \
    src/detection_layer.h \
    src/dropout_layer.h \
    src/gemm.h \
    src/gru_layer.h \
    src/im2col.h \
    src/image.h \
    src/iseg_layer.h \
    src/l2norm_layer.h \
    src/layer.h \
    src/list.h \
    src/local_layer.h \
    src/logistic_layer.h \
    src/lstm_layer.h \
    src/matrix.h \
    src/maxpool_layer.h \
    src/network.h \
    src/normalization_layer.h \
    src/option_list.h \
    src/parser.h \
    src/region_layer.h \
    src/reorg_layer.h \
    src/rnn_layer.h \
    src/route_layer.h \
    src/shortcut_layer.h \
    src/softmax_layer.h \
    src/stb_image.h \
    src/stb_image_write.h \
    src/tree.h \
    src/upsample_layer.h \
    src/utils.h \
    src/yolo_layer.h

SOURCES += \
    src/image_opencv.cpp \
    src/activation_layer.cpp \
    src/activations.cpp \
    src/avgpool_layer.cpp \
    src/batchnorm_layer.cpp \
    src/blas.cpp \
    src/box.cpp \
    src/col2im.cpp \
    src/compare.cpp \
    src/connected_layer.cpp \
    src/convolutional_layer.cpp \
    src/cost_layer.cpp \
    src/crnn_layer.cpp \
    src/crop_layer.cpp \
    src/cuda.cpp \
    src/data.cpp \
    src/deconvolutional_layer.cpp \
    src/demo.cpp \
    src/detection_layer.cpp \
    src/dropout_layer.cpp \
    src/gemm.cpp \
    src/gru_layer.cpp \
    src/im2col.cpp \
    src/image.cpp \
    src/iseg_layer.cpp \
    src/l2norm_layer.cpp \
    src/layer.cpp \
    src/list.cpp \
    src/local_layer.cpp \
    src/logistic_layer.cpp \
    src/lstm_layer.cpp \
    src/matrix.cpp \
    src/maxpool_layer.cpp \
    src/network.cpp \
    src/normalization_layer.cpp \
    src/option_list.cpp \
    src/parser.cpp \
    src/region_layer.cpp \
    src/reorg_layer.cpp \
    src/rnn_layer.cpp \
    src/route_layer.cpp \
    src/shortcut_layer.cpp \
    src/softmax_layer.cpp \
    src/tree.cpp \
    src/upsample_layer.cpp \
    src/utils.cpp \
    src/yolo_layer.cpp
