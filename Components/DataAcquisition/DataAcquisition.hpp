// ======================================================================
// \title  DataAcquisition.hpp
// \author sandersa
// \brief  hpp file for DataAcquisition component implementation class
// ======================================================================

#ifndef Manager_DataAcquisition_HPP
#define Manager_DataAcquisition_HPP

#include "Components/DataAcquisition/DataAcquisitionComponentAc.hpp"

namespace Manager {

class DataAcquisition final : public DataAcquisitionComponentBase {
  public:
    // ----------------------------------------------------------------------
    // Component construction and destruction
    // ----------------------------------------------------------------------

    //! Construct DataAcquisition object
    DataAcquisition(const char* const compName  //!< The component name
    );

    //! Destroy DataAcquisition object
    ~DataAcquisition();

  PRIVATE:
    // ----------------------------------------------------------------------
    // Handler implementations for commands
    // ----------------------------------------------------------------------

    //! Handler implementation for command TODO
    //!
    //! TODO
    void TODO_cmdHandler(FwOpcodeType opCode,  //!< The opcode
                         U32 cmdSeq            //!< The command sequence number
                         ) override;
};

}  // namespace Manager

#endif
