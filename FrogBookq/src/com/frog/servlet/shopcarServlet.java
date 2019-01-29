package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.frog.bean.Book;
import com.frog.bean.Cart;
import com.frog.dao.*;

public class shopcarServlet extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request,response);
	
	}


	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		HttpSession session=request.getSession();
		String username=(String) session.getAttribute("username");
		List<Cart> list=new CartDao().findByName(username);
		if(list==null){
			System.out.println("list¿Õ¿Õ");
		}
		request.setAttribute("AllKindCart", list);
		request.setAttribute("username", username);
		PrintWriter out=response.getWriter();
		if(username==null){
			request.getRequestDispatcher("jsp/nullInfo.jsp").forward(request, response);
		}else{
	      request.getRequestDispatcher("jsp/myshopcar.jsp").forward(request, response);
		}
	
	}

}
