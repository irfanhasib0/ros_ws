// Generated by gencpp from file pr2_gazebo_plugins/PlugCommand.msg
// DO NOT EDIT!


#ifndef PR2_GAZEBO_PLUGINS_MESSAGE_PLUGCOMMAND_H
#define PR2_GAZEBO_PLUGINS_MESSAGE_PLUGCOMMAND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pr2_gazebo_plugins
{
template <class ContainerAllocator>
struct PlugCommand_
{
  typedef PlugCommand_<ContainerAllocator> Type;

  PlugCommand_()
    : ac_present(false)
    , charge_rate(0.0)
    , discharge_rate(0.0)
    , charge(0.0)  {
    }
  PlugCommand_(const ContainerAllocator& _alloc)
    : ac_present(false)
    , charge_rate(0.0)
    , discharge_rate(0.0)
    , charge(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _ac_present_type;
  _ac_present_type ac_present;

   typedef double _charge_rate_type;
  _charge_rate_type charge_rate;

   typedef double _discharge_rate_type;
  _discharge_rate_type discharge_rate;

   typedef double _charge_type;
  _charge_type charge;





  typedef boost::shared_ptr< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> const> ConstPtr;

}; // struct PlugCommand_

typedef ::pr2_gazebo_plugins::PlugCommand_<std::allocator<void> > PlugCommand;

typedef boost::shared_ptr< ::pr2_gazebo_plugins::PlugCommand > PlugCommandPtr;
typedef boost::shared_ptr< ::pr2_gazebo_plugins::PlugCommand const> PlugCommandConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pr2_gazebo_plugins

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/melodic/share/nav_msgs/cmake/../msg'], 'pr2_gazebo_plugins': ['/home/irfan/Desktop/ros_ws/src/pr2/pr2_simulator/pr2_gazebo_plugins/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'pr2_msgs': ['/home/irfan/Desktop/ros_ws/src/pr2/pr2_common/pr2_msgs/msg'], 'diagnostic_msgs': ['/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "852b7035ee3e7fa6390824cf7b7e6dd1";
  }

  static const char* value(const ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x852b7035ee3e7fa6ULL;
  static const uint64_t static_value2 = 0x390824cf7b7e6dd1ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pr2_gazebo_plugins/PlugCommand";
  }

  static const char* value(const ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool ac_present\n"
"float64 charge_rate\n"
"float64 discharge_rate\n"
"float64 charge\n"
;
  }

  static const char* value(const ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ac_present);
      stream.next(m.charge_rate);
      stream.next(m.discharge_rate);
      stream.next(m.charge);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlugCommand_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pr2_gazebo_plugins::PlugCommand_<ContainerAllocator>& v)
  {
    s << indent << "ac_present: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ac_present);
    s << indent << "charge_rate: ";
    Printer<double>::stream(s, indent + "  ", v.charge_rate);
    s << indent << "discharge_rate: ";
    Printer<double>::stream(s, indent + "  ", v.discharge_rate);
    s << indent << "charge: ";
    Printer<double>::stream(s, indent + "  ", v.charge);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PR2_GAZEBO_PLUGINS_MESSAGE_PLUGCOMMAND_H