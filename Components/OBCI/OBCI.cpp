// ======================================================================
// \title  OBCI.cpp
// \author sandersa
// \brief  cpp file for OBCI component implementation class
// ======================================================================

#include "Components/OBCI/OBCI.hpp"

namespace Manager{

// ----------------------------------------------------------------------
// Component construction and destruction
// ----------------------------------------------------------------------

OBCI::OBCI(const char* const compName) : OBCIComponentBase(compName){}

OBCI::~OBCI(){}

// ----------------------------------------------------------------------
// Handler implementations for commands
// ----------------------------------------------------------------------

void OBCI::StartExperiment_cmdHandler(FwOpcodeType opCode, U32 cmdSeq){
    // TODO
    this->cmdResponse_out(opCode, cmdSeq, Fw::CmdResponse::OK);
}

void OBCI::StopExperiment_cmdHandler(FwOpcodeType opCode, U32 cmdSeq){
    // TODO
    this->cmdResponse_out(opCode, cmdSeq, Fw::CmdResponse::OK);
}

// ----------------------------------------------------------------------
// Handler implementations for typed input ports
// ----------------------------------------------------------------------

void OBCI::Tick_handler(FwIndexType portNum, U32 context){
    // TODO
}

}  // namespace Manager
