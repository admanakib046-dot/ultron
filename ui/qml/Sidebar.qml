import QtQuick
import QtQuick.Controls

Rectangle {

    width: 280
    color: "#080B10"

    Rectangle {

        anchors.fill: parent
        anchors.margins: 12

        radius: 25

        color: "#0D1117"

        border.color: "#1E2630"
        border.width: 1

        Column {

            anchors.fill: parent
            anchors.margins: 20

            spacing: 18

            //==========================
            // LOGO
            //==========================

            Column {

                width: parent.width

                spacing: 5

                Text {

                    text: "          ULTRON"
                    width: parent.width
                    horizontalAlignment: Text.AlignHCenter
                    color: "#FF2020"

                    font.family: "Orbitron"
                    font.pixelSize: 34
                    font.bold: true

                   
                }

                Text {

                    text: "                   AI ASSISTANT"
                    width: parent.width
                    horizontalAlignment: Text.AlignHCenter
                    color: "white"

                    opacity: 0.85

                    font.family: "Orbitron"
                    font.pixelSize: 16

                    
                }

                Rectangle {

                    width: parent.width
                    height: 1

                    color: "#20252D"
                }

            }

            //==========================
            // MENU
            //==========================

            Column {

                spacing: 12

                Repeater {

                    model: [
                        "HOME",
                        "VISION",
                        "VOICE",
                        "SYSTEM",
                        "MEMORY",
                        "INTERNET",
                        "AUTOMATION",
                        "SETTINGS"
                    ]

                    delegate: Rectangle {

                        id: button

                        width: 200
                        height: 46

                        radius: 12

                        property bool hovered: false

                        color: hovered ? "#1B212A" :
                               index===0 ? "#161B22" :
                               "transparent"

                        border.width: hovered || index===0 ? 2 : 1

                        border.color: hovered || index===0 ?
                                      "#FF3030" :
                                      "#2A313B"

                        scale: hovered ? 1.03 : 1.0

                        Behavior on scale {

                            NumberAnimation {
                                duration: 150
                            }

                        }

                        Behavior on color {

                            ColorAnimation {
                                duration: 150
                            }

                        }

                        // Left Red Indicator

                        Rectangle {

                            visible: hovered || index===0

                            width: 4
                            height: 26

                            radius: 2

                            color: "#FF3030"

                            anchors.left: parent.left
                            anchors.leftMargin: 8

                            anchors.verticalCenter: parent.verticalCenter
                        }

                        Text {

                            anchors.centerIn: parent

                            text: modelData

                            color: "white"

                            font.family: "Orbitron"
                            font.pixelSize: 15
                            font.bold: true
                        }

                        MouseArea {

                            anchors.fill: parent

                            hoverEnabled: true

                            cursorShape: Qt.PointingHandCursor

                            onEntered: button.hovered = true
                            onExited: button.hovered = false

                        }

                    }

                }

            }

            Item {

                width: 1
                height: 25

            }

            //==========================
            // POWER CARD
            //==========================

            Rectangle {

                width: 200
                height: 120

                radius: 18

                color: "#10151C"

                border.color: "#252C35"
                border.width: 1

                Column {

                    anchors.fill: parent
                    anchors.margins: 15

                    spacing: 8

                    Text {

                        text: "POWER STATUS"

                        color: "#AAAAAA"

                        font.family: "Orbitron"
                        font.pixelSize: 13
                    }

                    Text {

                        text: "100%"

                        color: "#FF2020"

                        font.family: "Orbitron"
                        font.pixelSize: 34
                        font.bold: true
                    }

                    Text {

                        text: "SYSTEM STABLE"

                        color: "#BBBBBB"

                        font.family: "Orbitron"
                        font.pixelSize: 12
                    }

                }

            }

            //==========================
            // CORE STATUS
            //==========================

            Rectangle {

                width: 200
                height: 70

                radius: 18

                color: "#10151C"

                border.color: "#252C35"
                border.width: 1

                Row {

                    anchors.fill: parent
                    anchors.margins: 15

                    spacing: 12

                    Text {

                        text: "ULTRON"

                        color: "#DDDDDD"

                        font.family: "Orbitron"
                        font.pixelSize: 14
                    }

                    Rectangle {

                        width: 14
                        height: 14

                        radius: 7

                        color: "#00FF66"

                        anchors.verticalCenter: parent.verticalCenter

                        SequentialAnimation on opacity {

                            loops: Animation.Infinite

                            NumberAnimation {
                                from: 1
                                to: 0.3
                                duration: 700
                            }

                            NumberAnimation {
                                from: 0.3
                                to: 1
                                duration: 700
                            }

                        }

                    }

                }

            }

        }

    }

}