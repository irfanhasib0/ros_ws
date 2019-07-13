
(cl:in-package :asdf)

(defsystem "ur5_notebook-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Tracker" :depends-on ("_package_Tracker"))
    (:file "_package_Tracker" :depends-on ("_package"))
    (:file "blocks_poses" :depends-on ("_package_blocks_poses"))
    (:file "_package_blocks_poses" :depends-on ("_package"))
  ))