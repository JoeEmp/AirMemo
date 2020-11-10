import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2
import "."

Rectangle {
    property bool isShow: false
    property alias text: t.text     // 显示的文字
    width : t.width + 5
    height: t.height
    //z: 100
    color: "#666666"
    opacity: isShow ? 1 : 0
    //border.width: units.dp(1)
    //border.color: "white"
    radius: 5

    Behavior on opacity {
        NumberAnimation { duration: 1000 }
    }

    Text{
        id:t
        anchors.centerIn: parent
        color:"white"
        text:""
    }

    Timer {
        id: toastTimer
        interval: 1000
        onTriggered: isShow = false
    }

    // 显示toast函数
    function show_toast() {
        isShow = true;
        toastTimer.restart();
    }

    // 获取长度
    function width() {
        return t.width + 5;
    }

    // 设置toast文本
    function set_text(text){
        t.text = ' '+text+' ';
    }

    // 设置定时器时长，毫秒级别
    function set_time(time){
        toastTimer.interval = time;
    }
}