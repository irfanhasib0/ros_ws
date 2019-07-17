
"use strict";

let AccessPoint = require('./AccessPoint.js');
let PressureState = require('./PressureState.js');
let BatteryState = require('./BatteryState.js');
let PowerBoardState = require('./PowerBoardState.js');
let GPUStatus = require('./GPUStatus.js');
let LaserTrajCmd = require('./LaserTrajCmd.js');
let BatteryServer2 = require('./BatteryServer2.js');
let PeriodicCmd = require('./PeriodicCmd.js');
let AccelerometerState = require('./AccelerometerState.js');
let PowerState = require('./PowerState.js');
let BatteryState2 = require('./BatteryState2.js');
let DashboardState = require('./DashboardState.js');
let LaserScannerSignal = require('./LaserScannerSignal.js');
let BatteryServer = require('./BatteryServer.js');

module.exports = {
  AccessPoint: AccessPoint,
  PressureState: PressureState,
  BatteryState: BatteryState,
  PowerBoardState: PowerBoardState,
  GPUStatus: GPUStatus,
  LaserTrajCmd: LaserTrajCmd,
  BatteryServer2: BatteryServer2,
  PeriodicCmd: PeriodicCmd,
  AccelerometerState: AccelerometerState,
  PowerState: PowerState,
  BatteryState2: BatteryState2,
  DashboardState: DashboardState,
  LaserScannerSignal: LaserScannerSignal,
  BatteryServer: BatteryServer,
};
