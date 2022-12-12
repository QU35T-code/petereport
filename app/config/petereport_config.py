PETEREPORT_CONFIG = {
	'admin_username': 'admin',
	'admin_password': 'Password1!',
	'admin_email': 'admin@qu35t.pw',
	'viewer_username': 'guest',
	'viewer_password': 'aAwHQp96rnW@dHCT.q',
	'viewer_email': 'guest@qu35t.pw'
}

DEFECTDOJO_CONFIG = {
	'DefectDojoURL': 'https://demo.defectdojo.org',
	'apiKey': 'Token <Key>' # Format: Token <api_key>
}

DJANGO_CONFIG = {
	'secret_key': 'django-insecure-key-CHANGEMEPLEASE-pKj9bd9h7*RMCuU',
	'debug': True,
	'admin_module': False,
	'allowed_hosts': '[\'*\']',
	'server_host': 'http://127.0.0.1:8000',
	'upload_memory_size': 10485760 # 10MB
}

PETEREPORT_TEMPLATES = {
	'templates_root': 'preport/templates/tpl',
	'storage_reports': 'storage_reports',
	'html_template': 'bootstrap-4-pandoc-template/template.html',
	'pdf_latex_template': 'petereport.latex',
	'report_id_format': 'PEN-DOC-',
	'report_csv_name': 'PEN-CSV',
	'report_markdown_name': 'PEN-MD',
	'report_html_name': 'PEN-HTML',
	'report_pdf_name': 'PEN-PDF',
	'report_pdf_language': "en",
	'report_pdf_title_background': "title.png", # title.png, blank.png - location: app/preport/templates/tpl/pdf/
	'report_pdf_pages_background': "title.png", # title.png, blank.png - location: app/preport/templates/tpl/pdf/
	'report_jupyter_name': 'PEN-JUPYTER',
	'initial_text': 'TBC',
	'titlepage-color': "e6e2e2",
	'titlepage-text-color': "000000",
	'titlepage-rule-color': "cc0000",
	'titlepage-rule-height': 2
}

PETEREPORT_MARKDOWN = {
	'author': 'QU35T Corporation',
	'subject': 'Pentest Report',
    'website': '',
	'martor_upload_method': 'BASE64', # BASE64 (stored in DB) or MEDIA (path not protected, must be set 'debug': True. This is highly insecure and not encouraged for production use. Should be configured the web server (apache, nginx, etc) to serve the media content using a protected link) 
	'media_host': 'http://127.0.0.1:8000' # If docker deployment, set https://<HOST IP>, else for django deployment http://<HOST IP>:8000 
}
