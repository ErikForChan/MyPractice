package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.frog.bean.Book;
import com.frog.dao.BookDao;

public class TypeServlet extends HttpServlet {


	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request,response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html;charset=utf-8");
		String bookType="science";
		List<Book> list=new BookDao().findBooksByType(bookType);
		request.setAttribute("AllKindBook", list);
		request.getRequestDispatcher("jsp/showbook.jsp").forward(request, response);
	
	}

}
