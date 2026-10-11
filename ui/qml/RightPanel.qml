import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    width: 340
    color: "transparent"

    ScrollView {
        anchors.fill: parent
        clip: true

        ScrollBar.vertical.policy: ScrollBar.AsNeeded
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff

        ColumnLayout {
            width: parent.width
            spacing: 12

            CameraCard {
                Layout.fillWidth: true
                Layout.preferredHeight: 250
            }

            MemoryCard {
                Layout.fillWidth: true
                Layout.preferredHeight: 300
            }

            NetworkCard {
                Layout.fillWidth: true
                Layout.preferredHeight: 250
            }

            SystemCard {
                Layout.fillWidth: true
                Layout.preferredHeight: 350
            }
        }
    }
}