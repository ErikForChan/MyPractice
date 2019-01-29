package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.frog.dao.JdbcUtil;

public class loginServlet extends HttpServlet {

	
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

        String username=request.getParameter("username");
        String password=request.getParameter("password");
        boolean flag=false; 
		response.setContentType("text/html;charset=utf-8");
        Connection con=null;
       
        try{	
        	con=JdbcUtil.getConnection();
			String sql="Select * from user where username=? and password=?;";
			PreparedStatement ps=con.prepareStatement(sql);
			ps.setString(1,username);
			ps.setString(2,password);
			ResultSet rs=ps.executeQuery();
			if(rs.next()){
				flag=true;				
			}
			rs.close();
			ps.close();
			con.close();
        	
        }catch(SQLException e){
        	e.printStackTrace();
        }
		
		response.setContentType("text/html;charset=UTF-8");
    
        	if(flag){
        		
        	HttpSession session=request.getSession();
            session.setAttribute("username", new String(username));	
        	request.getRequestDispatcher("/index.jsp").forward(request, response);
        	
            }else{
        	
            	request.getRequestDispatcher("jsp/loginError.jsp").forward(request, response);
        	
            }
   
		
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		doGet(request,response);   
		
	}

}
