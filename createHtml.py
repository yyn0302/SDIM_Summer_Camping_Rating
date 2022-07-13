#coding:utf-8
 
import webbrowser
 
#命名生成的html
GEN_HTML = "test.html" 
 
#打开文件，准备写入
f = open(GEN_HTML,'w')
 
#准备相关变量
str1 = 'my name is :'
str2 = '--MichaelAn--'
 
# 写入HTML界面中
message = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SDIM Summer Camping Rating Radar</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.js"></script>
</head>
<body>
    <style>
        #radarchart,
        html,
        body {
          width: 100%;
        }
        #radarchart {
          height: 400px;
        }
    </style>
    <div id="radarchart"></div>
    <script type="text/javascript">
        window.onresize = function () {
          myChart.resize();
        }
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('radarchart'));
    
          // 指定图表的配置项和数据
          var option = {
        title: {
          text: 'Week 1 Radar Chart'
        },
        legend: {
          data: ['Class Average', 'Your score']
        },
        radar: {
          // shape: 'circle',
          indicator: [
            { name: 'Knowledge Aquisition', max: 5 },
            { name: 'Motivation', max: 5 },
            { name: 'Communication', max: 5 },
            { name: 'Hands-On Skills', max: 5 },
            { name: 'Thinking Skills', max: 5 },
            { name: 'Responsibility', max: 5 },
            { name: 'Project Execution', max: 5 },
          ]
        },
        series: [
          {
            name: 'ratinng',
            type: 'radar',
            data: [
              {
                value: [3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5],
                name: 'Class Average',
                label: {
                    normal: {
                        show: true,
                        formatter:function(params) {
                            return params.value;}
                        }
                    }
              },
              {
                value: [4.0, 5.0, 3.5, 4.2, 1.0, 4.5, 4.9],
                name: 'Your score',
                label: {
                    normal: {
                        show: true,
                        formatter:function(params) {
                            return params.value;}
                        }
                    }
              }
            ]
          }
        ]
      };
      myChart.setOption(option);
      </script>
</body>
</html>
"""%(str1,str2)
 
#写入文件
f.write(message) 
 
#关闭文件
f.close()
 
#运行完自动在网页中显示
webbrowser.open(GEN_HTML,new = 1) 
'''
webbrowser.open(url, new=0, autoraise=True) 
Display url using the default browser. 
If new is 0, the url is opened in the same browser window if possible.
If new is 1, a new browser window is opened if possible.
If new is 2, a new browser page (“tab”) is opened if possible.
If auto raise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable).
'''