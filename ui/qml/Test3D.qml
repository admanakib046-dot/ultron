import QtQuick
import QtQuick.Window
import QtQuick3D

Window {
    visible: true
    width: 800
    height: 600
    color: "black"

    View3D {
        anchors.fill: parent

        environment: SceneEnvironment {
            backgroundMode: SceneEnvironment.Color
            clearColor: "black"
        }

        PerspectiveCamera {
            position: Qt.vector3d(0, 0, 600)
        }

        DirectionalLight {
            brightness: 50
        }

        Model {
            source: "#Sphere"

            materials: DefaultMaterial {
                diffuseColor: "#ff3030"
                
            }

            NumberAnimation on eulerRotation.y {
                from: 0
                to: 360
                duration: 6000
                loops: Animation.Infinite
            }
        }
    }
}