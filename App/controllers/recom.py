import jinja2
import os
from jinja2 import Template
import pdflatex
from pdflatex import PDFLaTeX, JINJA2_ENV

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)


def generate_recom():
  
    body = 'Short Form'
    author = 'Mr. John Young'
    position = 'Teacher'
    student = 'Ricky Bob'

    env = JINJA2_ENV
    env['loader'] = jinja2.FileSystemLoader(os.path.abspath('.'))
    env = jinja2.Environment(**env)
    template = env.get_template('./App/main.tex')
    pdfl = PDFLaTeX.from_jinja_template(template, jobname='output.pdf', body=body, author=author, position=position, student=student)
    pdf, log, cp = pdfl.create_pdf()