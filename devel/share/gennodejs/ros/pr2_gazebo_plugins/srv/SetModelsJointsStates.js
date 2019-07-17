// Auto-generated. Do not edit!

// (in-package pr2_gazebo_plugins.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ModelJointsState = require('../msg/ModelJointsState.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetModelsJointsStatesRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.model_names = null;
      this.model_joints_states = null;
    }
    else {
      if (initObj.hasOwnProperty('model_names')) {
        this.model_names = initObj.model_names
      }
      else {
        this.model_names = [];
      }
      if (initObj.hasOwnProperty('model_joints_states')) {
        this.model_joints_states = initObj.model_joints_states
      }
      else {
        this.model_joints_states = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetModelsJointsStatesRequest
    // Serialize message field [model_names]
    bufferOffset = _arraySerializer.string(obj.model_names, buffer, bufferOffset, null);
    // Serialize message field [model_joints_states]
    // Serialize the length for message field [model_joints_states]
    bufferOffset = _serializer.uint32(obj.model_joints_states.length, buffer, bufferOffset);
    obj.model_joints_states.forEach((val) => {
      bufferOffset = ModelJointsState.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetModelsJointsStatesRequest
    let len;
    let data = new SetModelsJointsStatesRequest(null);
    // Deserialize message field [model_names]
    data.model_names = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [model_joints_states]
    // Deserialize array length for message field [model_joints_states]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.model_joints_states = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.model_joints_states[i] = ModelJointsState.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.model_names.forEach((val) => {
      length += 4 + val.length;
    });
    object.model_joints_states.forEach((val) => {
      length += ModelJointsState.getMessageSize(val);
    });
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pr2_gazebo_plugins/SetModelsJointsStatesRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ecf71b483df7b70447575a8231727200';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] model_names
    pr2_gazebo_plugins/ModelJointsState[] model_joints_states
    
    ================================================================================
    MSG: pr2_gazebo_plugins/ModelJointsState
    geometry_msgs/Pose[] model_pose                          # set as single element array if user wishes to specify model pose, otherwise, leave empty
    string[] joint_names                                     # list of joint names
    float64[] joint_positions                                 # list of desired joint positions, should match joint_names
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetModelsJointsStatesRequest(null);
    if (msg.model_names !== undefined) {
      resolved.model_names = msg.model_names;
    }
    else {
      resolved.model_names = []
    }

    if (msg.model_joints_states !== undefined) {
      resolved.model_joints_states = new Array(msg.model_joints_states.length);
      for (let i = 0; i < resolved.model_joints_states.length; ++i) {
        resolved.model_joints_states[i] = ModelJointsState.Resolve(msg.model_joints_states[i]);
      }
    }
    else {
      resolved.model_joints_states = []
    }

    return resolved;
    }
};

class SetModelsJointsStatesResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
      this.status_message = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
      if (initObj.hasOwnProperty('status_message')) {
        this.status_message = initObj.status_message
      }
      else {
        this.status_message = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetModelsJointsStatesResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    // Serialize message field [status_message]
    bufferOffset = _serializer.string(obj.status_message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetModelsJointsStatesResponse
    let len;
    let data = new SetModelsJointsStatesResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [status_message]
    data.status_message = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.status_message.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pr2_gazebo_plugins/SetModelsJointsStatesResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2ec6f3eff0161f4257b808b12bc830c2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    string status_message
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetModelsJointsStatesResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    if (msg.status_message !== undefined) {
      resolved.status_message = msg.status_message;
    }
    else {
      resolved.status_message = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: SetModelsJointsStatesRequest,
  Response: SetModelsJointsStatesResponse,
  md5sum() { return 'b3f4760ee77e28f605915bcee447b72d'; },
  datatype() { return 'pr2_gazebo_plugins/SetModelsJointsStates'; }
};
