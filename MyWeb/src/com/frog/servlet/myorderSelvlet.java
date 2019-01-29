package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.frog.bean.Cart;
import com.frog.bean.Order;
import com.frog.bean.User;
import com.frog.dao.CartDao;
import com.frog.dao.OrderDao;
import com.frog.dao.UserDao;

public class myorderSelvlet extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		doPost(request,response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		HttpSession session=request.getSession();
		String username=(String) session.getAttribute("username");
	    Date date=new Date();
	    DateFormat format=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
	    String time=format.format(date);
		System.out.println(username);
		List<Order> list=new OrderDao().findByName(username);
		User user=new UserDao().findByUserName(username);
		request.setAttribute("AllOrder", list);
		request.setAttribute("user", user);
		request.setAttribute("time", time);
		request.setAttribute("username", username);
		PrintWriter out=response.getWriter();
		if(list==null){
			System.out.println("list¿Õ¿Õ");
			request.getRequestDispatcher("jsp/nullInfo.jsp").forward(request, response);
		}else{
         request.getRequestDispatcher("jsp/myorder.jsp").forward(request, response);
		}
	}

}
