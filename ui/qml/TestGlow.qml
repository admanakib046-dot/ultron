import QtQuick
import QtQuick3D

View3D {
    anchors.fill: parent

    PerspectiveCamera {
        z: 300
    }

    environment: SceneEnvironment {
        backgroundMode: SceneEnvironment.Color
        clearColor: "black"
    }

    Model {
        source: "#Sphere"
        scale: Qt.vector3d(60, 60, 60)

        materials: PrincipledMaterial {
            baseColor: "white"
            emissiveFactor: Qt.vector3d(100, 100, 100)
            lighting: PrincipledMaterial.NoLighting
        }
    }
}