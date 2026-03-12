#include <iostream>
#include <vector>
#include <cstdint>

namespace tensoredge {

class Engine {
public:
    Engine() = default;

    void forward(const int8_t* input, const int8_t* weights, int32_t* output, 
                 int rows, int cols) {
        // Optimized Integer Matrix Multiplication
        for (int i = 0; i < rows; ++i) {
            int32_t sum = 0;
            for (int j = 0; j < cols; ++j) {
                sum += input[j] * weights[i * cols + j];
            }
            output[i] = sum;
        }
    }

    void relu(int32_t* data, int size) {
        for (int i = 0; i < size; ++i) {
            if (data[i] < 0) data[i] = 0;
        }
    }
};

} // namespace tensoredge
