#### Scrapy分门别类/批量下载土巴兔所有的装修图
##### 装修的DEMO案例与对应的图片文件(装修效果图)有很多，下载后的图片文件，也必须分门别类以利区分并方便管理，比如"60万288㎡现代简约家装装修效果图"内有3张属于该风格的效果图，以此类推，最终下载回来的是各种风格的完整案例，以及所有案例对应的装修效果图，最终以装修主名称作为文件夹的名称，以下是此项目执行后的结果图:
##### 1，结果截图
![img1](https://github.com/ziliang-wang/tubatu/blob/master/images/tubatu_1.png)
##### 2，spider爬虫文件里，有关"详情"解析函数parse_detail()的说明
![img4](https://github.com/ziliang-wang/tubatu/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200427163920.png)
###### 详情页返回的是json数据(json字符串)，所以需要使用json模块的loads()函数来将json字符串"反序列化"转成与python对应的数据结构，此项目对应的是python字典，同时在for循环体里，再加一个循环判断，判断当前的id是否等于上层解析函数parse()中meta传过来的装修id，判断时，要特别注意数据类型，xpath取出的是字符串，而json对应的字段是int，所以要先转成int后再比较，若不加循环判断的代码，就会全部抓取！

##### 3，ImagesPipeline关键代码块，代码非常的简单，理一下就能够理解代码逻辑！
![img3](https://github.com/ziliang-wang/tubatu/blob/master/images/tubatu_code.png)
