telemetry packets CerberusPackets {

  packet CDH id 1 group 1 {
    Cerberus.cmdDisp.CommandsDispatched
    Cerberus.rateGroup1.RgMaxTime
    Cerberus.rateGroup2.RgMaxTime
    Cerberus.rateGroup3.RgMaxTime
    Cerberus.cmdSeq.CS_LoadCommands
    Cerberus.cmdSeq.CS_CancelCommands
    Cerberus.cmdSeq.CS_CommandsExecuted
    Cerberus.cmdSeq.CS_SequencesCompleted
    Cerberus.fileUplink.FilesReceived
    Cerberus.fileUplink.PacketsReceived
    Cerberus.bufferManager.TotalBuffs
    Cerberus.bufferManager.CurrBuffs
    Cerberus.bufferManager.HiBuffs
    Cerberus.fileDownlink.FilesSent
    Cerberus.fileDownlink.PacketsSent
    Cerberus.fileManager.CommandsExecuted
    Cerberus.comQueue.comQueueDepth
    Cerberus.comQueue.buffQueueDepth
    # Note: Uncomment when using Svc:TlmPacketizer
    # Cerberus.tlmSend.SendLevel
  }

  packet CDHErrors id 2 group 1 {
    Cerberus.rateGroup1.RgCycleSlips
    Cerberus.rateGroup2.RgCycleSlips
    Cerberus.rateGroup3.RgCycleSlips
    Cerberus.cmdSeq.CS_Errors
    Cerberus.fileUplink.Warnings
    Cerberus.fileDownlink.Warnings
    Cerberus.$health.PingLateWarnings
    Cerberus.fileManager.Errors
    Cerberus.bufferManager.NoBuffs
    Cerberus.bufferManager.EmptyBuffs
    Cerberus.fileManager.Errors
  }

  packet SystemRes1 id 4 group 2 {
    Cerberus.systemResources.MEMORY_TOTAL
    Cerberus.systemResources.MEMORY_USED
    Cerberus.systemResources.NON_VOLATILE_TOTAL
    Cerberus.systemResources.NON_VOLATILE_FREE
  }

  packet SystemRes3 id 5 group 2 {
    Cerberus.systemResources.CPU
    Cerberus.systemResources.CPU_00
    Cerberus.systemResources.CPU_01
    Cerberus.systemResources.CPU_02
    Cerberus.systemResources.CPU_03
    Cerberus.systemResources.CPU_04
    Cerberus.systemResources.CPU_05
    Cerberus.systemResources.CPU_06
    Cerberus.systemResources.CPU_07
    Cerberus.systemResources.CPU_08
    Cerberus.systemResources.CPU_09
    Cerberus.systemResources.CPU_10
    Cerberus.systemResources.CPU_11
    Cerberus.systemResources.CPU_12
    Cerberus.systemResources.CPU_13
    Cerberus.systemResources.CPU_14
    Cerberus.systemResources.CPU_15
  }

  packet Version1 id 6 group 2 {
    Cerberus.version.FrameworkVersion
    Cerberus.version.ProjectVersion
  }

  packet Version_Library1 id 7 group 2 {
    Cerberus.version.LibraryVersion01
    Cerberus.version.LibraryVersion02
  }

  packet Version_Library2 id 8 group 2 {
    Cerberus.version.LibraryVersion03
    Cerberus.version.LibraryVersion04
  }

  packet Version_Library3 id 9 group 2 {
    Cerberus.version.LibraryVersion05
    Cerberus.version.LibraryVersion06
  }

  packet Version_Library4 id 10 group 2 {
    Cerberus.version.LibraryVersion07
    Cerberus.version.LibraryVersion08
  }

  packet Version_Library5 id 11 group 2 {
    Cerberus.version.LibraryVersion09
    Cerberus.version.LibraryVersion10
  }

  packet Version_Custom1 id 12 group 2 {
    Cerberus.version.CustomVersion01
  }

  packet Version_Custom2 id 13 group 2 {
    Cerberus.version.CustomVersion02
  }

  packet Version_Custom3 id 14 group 2 {
    Cerberus.version.CustomVersion03
  }

  packet Version_Custom4 id 15 group 2 {
    Cerberus.version.CustomVersion04
  }

  packet Version_Custom5 id 16 group 2 {
    Cerberus.version.CustomVersion05
  }

  packet Version_Custom6 id 17 group 2 {
    Cerberus.version.CustomVersion06
  }

  packet Version_Custom7 id 18 group 2 {
    Cerberus.version.CustomVersion07
  }

  packet Version_Custom8 id 19 group 2 {
    Cerberus.version.CustomVersion08
  }

  packet Version_Custom9 id 20 group 2 {
    Cerberus.version.CustomVersion09
  }

  packet Version_Custom10 id 21 group 2 {
    Cerberus.version.CustomVersion10
  }

} omit {
  Cerberus.cmdDisp.CommandErrors
}
