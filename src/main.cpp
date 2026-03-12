#include "engine.hpp"
#include <iostream>

int main() {
    tensoredge::Engine engine;
    
    int8_t input[4] = {10, -5, 20, 1};
    int8_t weights[8] = {1, 2, 3, 4, -1, -2, -3, -4};
    int32_t output[2] = {0, 0};

    engine.forward(input, weights, output, 2, 4);
    
    std::cout << "Inference Output: " << output[0] << ", " << output[1] << std::endl;
    
    return 0;
}
