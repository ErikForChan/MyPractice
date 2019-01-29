<%@page import="java.sql.*"%>
<%@page import="javax.naming.*"%>
<%@page import="javax.activation.DataSource"%>
<%@page import="com.frog.dao.*"%>
<%@page import="com.frog.bean.*"%>
<%@ page language="java" import="com.frog.bean.User" %>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'addCartHandler.jsp' starting page</title>

  </head>
  
  <body>
  
    <%
    
      String bookname=request.getParameter("bookname");
      String imageurl=request.getParameter("imageurl");
      String p=request.getParameter("price");
      int price=Integer.parseInt(p);
       System.out.println(bookname);
         System.out.println(imageurl);
         System.out.println(price);
     // Book book=(Book)request.getSession().getAttribute("book");
      boolean flag=false;
      Connection con=null;
      PreparedStatement pst=null;
        try{
        System.out.println("111");
        con=JdbcUtil.getConnection();
        con.setAutoCommit(false);		    
        String sql="insert into cart(username,imgURL,bookname,price,count,totalprice)values(?,?,?,?,?,?);";
        pst=con.prepareStatement(sql);
        System.out.println("222");
		   pst.setString(1,bookname);
		   pst.setString(2,imageurl);	 
		   pst.setString(3,bookname);           		
		   pst.setInt(4,price);
		   pst.setInt(5,1);
		   pst.setInt(6,1);
		   System.out.println("333");
		   pst.executeUpdate();
		   System.out.println("444");
		   con.commit();
		   flag=true;
		   pst.close();
		   con.close();
		}catch(Exception e){
		e.printStackTrace();
		} 
         
              if(flag){
              request.getRequestDispatcher("myshopcar.jsp").forward(request,response);          
                 
              }else{
                  out.print("加入购物车失败!");
              }
	   
     %>
  </body>
</html>
