<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ page contentType="text/html;charset=utf-8"%> 
<%@page import="com.frog.dao.*"%>
<%@page import="com.frog.bean.*"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
     <link rel="stylesheet" type="text/css" href="<%=path %>/css/myorder.css"/>
    <title>My JSP 'myorder.jsp' starting page</title>
   
  
  <body>
  
    <div class="top">
    
    <div class="info">
    <div class="time"><script style="align:right"> 
    document.write("<span id=time></span>") //输出显示时间日期的容器 
    //每1000毫秒(即1秒) 执行一次本段代码 
    setInterval("time.innerText=new Date().toLocaleString()",1000)  
      </script></div>
    <div class="username"><marquee behivior="alternate">在线用户： <%=request.getAttribute("username") %></marquee scrollAmount=></div>
    <div class="shoppingcar"></div>
    <div class="login"><a href="jsp/login.jsp" target="_top"><input type="button" value="登陆" ></input></a></div>
    <div class="register"><a href="jsp/register.jsp" target="_top"><input type="button" value="注册"></input></a></div>  
    <div class="logout"><a href="logoutServlet" target="_top"><input type="button" value="注销"></input></a></div>  
    </div>
   
    <div class="washu">
    	<a href="index.jsp"><div class="logo"></div></a>
    	<div class="myshopcar"></div>
    </div>
    </div>
    
    <hr style="background-color:#8fd6f5;height:3px;">
  
   
    <div class="orderform">
    
     <div class="myorder"><tr class="myordersize">我的订单<tr></div>
     <tr height="30" width="240"><div class="booktitle">商品信息：</div></tr><br/>  
  
     <div class="bookinfo"> 
    
     <%
             List<Order> list=(List<Order>)request.getAttribute("AllOrder");
             User user=(User)request.getAttribute("user");
             Iterator<Order> it=null;
             int Total=0;
             if(list==null){System.out.println("list为空");}
          
             if(list!=null){
             it=list.iterator();
             }
             Order order=null;
         
             while(it.hasNext()){
                 order=it.next();      
                 Total+=order.getTotalprice();      
                 request.getSession().setAttribute("username",order.getUsername());           
                 request.getSession().setAttribute("bookname",order.getBookname());
             %> 
                 <table style="border-style:dashed; border-width:1px; border-color:#00a0e9;" width="800px">
                 <tr height="30" width="800" align="center">
                       <td height="30" width="200" align="center">名称：<%=order.getBookname() %></td>
                       <td height="30" width="200" align="center">单价：<%=order.getPrice() %></td>
                       <td height="30" width="200" align="center">数量：<%=order.getCount() %></td>
                       <td height="30" width="200" align="center">价格：<%=order.getTotalprice() %></td><br/>
                  </tr> 
                  </table>

            <%
              }   
               new OrderDao().cutOrder();    
               
            %>    
            <table style="border-style:dashed; border-width:1px; border-color:#00a0e9;" width="800px"> 
            <tr height="30" width="800" align="center">
                       <td height="30" width="200" align="center"></td>
                       <td height="30" width="200" align="center"></td>
                       <td height="30" width="200" align="center"></td>
                       <td height="30" width="200" align="center"><B style="font-size: 20px">应付金额：<%=Total %>元</B></td><br/>
            </tr> 
            </table>
  
      </div>
      
            <tr height="30" width="240"><div class="usertitle">收货人信息：</div></tr><br/>  
            <div class="userinfo"> 
            <table cellpadding="1"  style="border-style:dashed; border-width:1px; border-color:#00a0e9;">
            <tr height="30" width="800">
              		   <td height="30" width="200" align="center">姓名：<%=user.getUsername() %></td>
              		   <td height="30" width="200" align="center">订购时间：<%=request.getAttribute("time") %></td>
                       <td height="30" width="200" align="center">电话：<%=user.getPhone() %></td>
                       <td height="30" width="200" align="center">地址：<%=user.getAddress() %></td><br/>                    
            </tr>
            <table>
          
            </div>
            <div class="pay">
            <a href="deleteOrderServlet"> 
            <input type="button" value="付款"/><br/>
            </a></tr>
       
    
    </div>
  
     

    
    
  </body>
</html>
