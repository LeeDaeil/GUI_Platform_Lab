import QtQuick 2.12
import QtQuick.Window 2.0

Window {
    width: 640
    height: 480
    visible: true
    title: "Hello Python World!"

    Text {
        text: qsTr("Hello GUIplatform0")
        anchors.centerIn: parent
        font.family: Constants.font.family
    }

    Custombo0 {
        id: custombo0
        x: 401
        y: 315
        width: 58
        height: 61
    }

}