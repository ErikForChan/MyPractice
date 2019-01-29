package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.frog.bean.Book;
import com.frog.dao.JdbcUtil;

public class addCart extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		 response.setCharacterEncoding("UTF-8");
		 HttpSession session=request.getSession();
		 String username=(String) session.getAttribute("username");
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
	        String sql="insert into cart values(?,?,?,?,?,?);";
	        pst=con.prepareStatement(sql);
			   pst.setString(1,username);
			   pst.setString(2,imageurl);	 
			   pst.setString(3,bookname);           		
			   pst.setInt(4,price);
			   pst.setInt(5,1);
			   pst.setInt(6,price);
			   pst.executeUpdate();
			   con.commit();
			   flag=true;
			   pst.close();
			   con.close();
			}catch(Exception e){
			e.printStackTrace();
			} 
	        PrintWriter out=response.getWriter();	
	       if(flag){
	    	   out.print("Add Book To Cart Success!");

	        }else{
	                  out.print("加入购物车失败!");
	        }
	}


	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request,response);   
	}

}
