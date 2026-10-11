import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
id: window
visible: true
width: 1920
height: 1080
title: "ULTRON"
color: "#05070C"

property bool hudOpen: false

Rectangle {
    anchors.fill: parent
    color: "#05070C"
}

// =========================================================
// AI CORE
// =========================================================

Item {
    id: coreContainer

    width: window.hudOpen ? 650 : parent.width
    height: window.hudOpen ? 650 : parent.height

    anchors.centerIn: parent

    Behavior on width {
        NumberAnimation { duration: 600; easing.type: Easing.InOutCubic }
    }

    Behavior on height {
        NumberAnimation { duration: 600; easing.type: Easing.InOutCubic }
    }

    Core3D {
        anchors.fill: parent
    }
}

// =========================================================
// DASHBOARD
// =========================================================

Item {

    anchors.fill: parent

    visible: False

    opacity: window.hudOpen ? 1 : 0

    Behavior on opacity {
        NumberAnimation {
            duration: 450
        }
    }

    RowLayout {

        anchors.fill: parent
        anchors.margins: 12
        spacing: 12

        Sidebar {
            Layout.preferredWidth: 260
            Layout.fillHeight: true
        }

        ColumnLayout {

            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 12

            TopBar {
                Layout.fillWidth: true
                Layout.preferredHeight: 80
            }

            Dashboard {
                Layout.fillWidth: true
                Layout.fillHeight: true
            }

            VoiceBar {
                Layout.fillWidth: true
                Layout.preferredHeight: 90
            }
        }

        RightPanel {
            Layout.preferredWidth: 340
            Layout.fillHeight: true
        }
    }
}

// =========================================================
// ULTRON BUTTON
// =========================================================

Rectangle {

    id: hudButton

    width: 90
    height: 90
    radius: 45

    anchors.right: parent.right
    anchors.bottom: parent.bottom
    anchors.margins: 30

    color: "#10151F"

    border.color: "#FF3030"
    border.width: 3

    Text {

        anchors.centerIn: parent

        text: window.hudOpen ? "×" : "U"

        color: "#FF3030"

        font.pixelSize: 42
        font.bold: true
    }

    MouseArea {
        anchors.fill: parent

        onClicked: {
            window.hudOpen = !window.hudOpen
        }
    }

    SequentialAnimation on scale {

        loops: Animation.Infinite

        NumberAnimation {
            from: 1
            to: 1.08
            duration: 1200
        }

        NumberAnimation {
            from: 1.08
            to: 1
            duration: 1200
        }
    }
}

}