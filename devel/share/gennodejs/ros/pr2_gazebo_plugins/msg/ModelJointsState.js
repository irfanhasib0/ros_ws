// Auto-generated. Do not edit!

// (in-package pr2_gazebo_plugins.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class ModelJointsState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.model_pose = null;
      this.joint_names = null;
      this.joint_positions = null;
    }
    else {
      if (initObj.hasOwnProperty('model_pose')) {
        this.model_pose = initObj.model_pose
      }
      else {
        this.model_pose = [];
      }
      if (initObj.hasOwnProperty('joint_names')) {
        this.joint_names = initObj.joint_names
      }
      else {
        this.joint_names = [];
      }
      if (initObj.hasOwnProperty('joint_positions')) {
        this.joint_positions = initObj.joint_positions
      }
      else {
        this.joint_positions = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ModelJointsState
    // Serialize message field [model_pose]
    // Serialize the length for message field [model_pose]
    bufferOffset = _serializer.uint32(obj.model_pose.length, buffer, bufferOffset);
    obj.model_pose.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [joint_names]
    bufferOffset = _arraySerializer.string(obj.joint_names, buffer, bufferOffset, null);
    // Serialize message field [joint_positions]
    bufferOffset = _arraySerializer.float64(obj.joint_positions, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ModelJointsState
    let len;
    let data = new ModelJointsState(null);
    // Deserialize message field [model_pose]
    // Deserialize array length for message field [model_pose]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.model_pose = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.model_pose[i] = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [joint_names]
    data.joint_names = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [joint_positions]
    data.joint_positions = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 56 * object.model_pose.length;
    object.joint_names.forEach((val) => {
      length += 4 + val.length;
    });
    length += 8 * object.joint_positions.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pr2_gazebo_plugins/ModelJointsState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f700a74958b6566fae4cd77fbb80ffd4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new ModelJointsState(null);
    if (msg.model_pose !== undefined) {
      resolved.model_pose = new Array(msg.model_pose.length);
      for (let i = 0; i < resolved.model_pose.length; ++i) {
        resolved.model_pose[i] = geometry_msgs.msg.Pose.Resolve(msg.model_pose[i]);
      }
    }
    else {
      resolved.model_pose = []
    }

    if (msg.joint_names !== undefined) {
      resolved.joint_names = msg.joint_names;
    }
    else {
      resolved.joint_names = []
    }

    if (msg.joint_positions !== undefined) {
      resolved.joint_positions = msg.joint_positions;
    }
    else {
      resolved.joint_positions = []
    }

    return resolved;
    }
};

module.exports = ModelJointsState;
