#### Scrapy分门别类/批量下载土巴兔所有的装修图
##### 装修的DEMO案例与对应的图片文件(装修效果图)有很多，下载后的图片文件，也必须分门别类以利区分并方便管理，比如"60万288㎡现代简约家装装修效果图"内有3张属于该风格的效果图，以此类推，最终下载回来的是各种风格的完整案例，以及所有案例对应的装修效果图，最终以装修主名称作为文件夹的名称，以下是此项目执行后的结果图:
##### 结果截图1
![img1](https://github.com/ziliang-wang/tubatu/blob/master/images/tubatu_1.png)
##### ImagesPipeline关键代码块，代码非常的简单，理一下就能够理解代码逻辑！
![img3](https://github.com/ziliang-wang/tubatu/blob/master/images/tubatu_code.png)
