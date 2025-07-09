// ======================================================================
// \title  DataAcquisition.cpp
// \author sandersa
// \brief  cpp file for DataAcquisition component implementation class
// ======================================================================

#include "Components/DataAcquisition/DataAcquisition.hpp"

namespace Manager {

// ----------------------------------------------------------------------
// Component construction and destruction
// ----------------------------------------------------------------------

DataAcquisition ::DataAcquisition(const char* const compName) : DataAcquisitionComponentBase(compName) {}

DataAcquisition ::~DataAcquisition() {}

// ----------------------------------------------------------------------
// Handler implementations for commands
// ----------------------------------------------------------------------

void DataAcquisition ::TODO_cmdHandler(FwOpcodeType opCode, U32 cmdSeq) {
    // TODO
    this->cmdResponse_out(opCode, cmdSeq, Fw::CmdResponse::OK);
}

}  // namespace Manager
