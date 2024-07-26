#include <opencv2/opencv.hpp>
#include <iostream>

// Toma la imagen en escala de grises (cv::Mat)
// y lee los pixeles de X e Y.
// Si cualquier pixel es diferente a 0, devuelve false.
bool isImageBlack(const cv::Mat& img) {
    for (int y = 0; y < img.rows; ++y) {
        for (int x = 0; x < img.cols; ++x) {
            if (img.at<uint8_t>(y, x) != 0) {
                return false;
            }
        }
    }
    return true;
}

// Preferentemente utilizar path sin caracteres especiales
int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <image path>" << std::endl;
        return 1;
    }

    cv::Mat img = cv::imread(argv[1], cv::IMREAD_GRAYSCALE);
    if (img.empty()) {
        std::cerr << "Error: Could not open or find the image!" << std::endl;
        return 1;
    }

    // Devuelve el resultado bool de isImageBlack
    std::cout << isImageBlack(img);

    return 0;
}
