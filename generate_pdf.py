from weasyprint import HTML

HTML(string="<h1>Hello, PDF!</h1>").write_pdf("test.pdf")
print("PDF generated successfully!")
