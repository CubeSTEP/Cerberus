state machine SATMode {

  action CheckSafety
  action PerformExperiment
  action SafeCheck
  action SafeExit
  action SetUpExperiment
  action Startup
  action TearDownExperiment


  signal EndExperiment
  signal ErrorDetected
  signal SafeExit
  signal StartExperiment
  signal StartUpComplete
  signal Tick

  state StartUp {
   entry do { Startup }
    on StartUpComplete do { SafeCheck } enter Safe
  }

  state Safe {
    on SafeExit do { SafeExit } enter MonitorSafety
  }

  state MonitorSafety {
    state Idle {
      on StartExperiment do { SetUpExperiment } enter Experiment
    }

    state Experiment {
      on EndExperiment do { TearDownExperiment } enter Idle
      on Tick do { PerformExperiment }
    }

    initial enter Idle
    on ErrorDetected enter Safe
    on Tick do { CheckSafety }
  }

  initial enter StartUp
}
