// Auto-generated. Do not edit!

// (in-package pr2_gazebo_plugins.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class PlugCommand {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ac_present = null;
      this.charge_rate = null;
      this.discharge_rate = null;
      this.charge = null;
    }
    else {
      if (initObj.hasOwnProperty('ac_present')) {
        this.ac_present = initObj.ac_present
      }
      else {
        this.ac_present = false;
      }
      if (initObj.hasOwnProperty('charge_rate')) {
        this.charge_rate = initObj.charge_rate
      }
      else {
        this.charge_rate = 0.0;
      }
      if (initObj.hasOwnProperty('discharge_rate')) {
        this.discharge_rate = initObj.discharge_rate
      }
      else {
        this.discharge_rate = 0.0;
      }
      if (initObj.hasOwnProperty('charge')) {
        this.charge = initObj.charge
      }
      else {
        this.charge = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PlugCommand
    // Serialize message field [ac_present]
    bufferOffset = _serializer.bool(obj.ac_present, buffer, bufferOffset);
    // Serialize message field [charge_rate]
    bufferOffset = _serializer.float64(obj.charge_rate, buffer, bufferOffset);
    // Serialize message field [discharge_rate]
    bufferOffset = _serializer.float64(obj.discharge_rate, buffer, bufferOffset);
    // Serialize message field [charge]
    bufferOffset = _serializer.float64(obj.charge, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PlugCommand
    let len;
    let data = new PlugCommand(null);
    // Deserialize message field [ac_present]
    data.ac_present = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [charge_rate]
    data.charge_rate = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [discharge_rate]
    data.discharge_rate = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [charge]
    data.charge = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 25;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pr2_gazebo_plugins/PlugCommand';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '852b7035ee3e7fa6390824cf7b7e6dd1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool ac_present
    float64 charge_rate
    float64 discharge_rate
    float64 charge
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PlugCommand(null);
    if (msg.ac_present !== undefined) {
      resolved.ac_present = msg.ac_present;
    }
    else {
      resolved.ac_present = false
    }

    if (msg.charge_rate !== undefined) {
      resolved.charge_rate = msg.charge_rate;
    }
    else {
      resolved.charge_rate = 0.0
    }

    if (msg.discharge_rate !== undefined) {
      resolved.discharge_rate = msg.discharge_rate;
    }
    else {
      resolved.discharge_rate = 0.0
    }

    if (msg.charge !== undefined) {
      resolved.charge = msg.charge;
    }
    else {
      resolved.charge = 0.0
    }

    return resolved;
    }
};

module.exports = PlugCommand;
