// ======================================================================
// \title  OBCI.hpp
// \author sandersa
// \brief  hpp file for OBCI component implementation class
// ======================================================================

#ifndef Manager_OBCI_HPP
#define Manager_OBCI_HPP

#include "Components/OBCI/OBCIComponentAc.hpp"

namespace Manager {

class OBCI final : public OBCIComponentBase {
  public:
    // ----------------------------------------------------------------------
    // Component construction and destruction
    // ----------------------------------------------------------------------

    //! Construct OBCI object
    OBCI(const char* const compName  //!< The component name
    );

    //! Destroy OBCI object
    ~OBCI();

  PRIVATE:
    // ----------------------------------------------------------------------
    // Handler implementations for commands
    // ----------------------------------------------------------------------

    //! Handler implementation for command StartExperiment
    //!
    //! TODO
    void StartExperiment_cmdHandler(
      FwOpcodeType opCode,  //!< The opcode
      U32 cmdSeq            //!< The command sequence number
    ) override;

    //! Handler implementation for command StopExperiment
    void StopExperiment_cmdHandler(
      FwOpcodeType opCode,  //!< The opcode
      U32 cmdSeq            //!< The command sequence number
    ) override;

    // ----------------------------------------------------------------------
    // Handler implementations for typed input ports
    // ----------------------------------------------------------------------

    //! Handler implementation for Tick
    //!
    //! Rate group scheduling
    void Tick_handler(
      FwIndexType portNum,  //!< The port number
      U32 context           //!< The call order
    ) override;
};

}  // namespace Manager

#endif
