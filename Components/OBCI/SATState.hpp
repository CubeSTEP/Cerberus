#include <cstdint>

namespace Manager{
    enum class SATState : int8_t{
        Safe = -1,
        StartUp = 0,
        Idle = 1,
        Experiment = 2
    };
}