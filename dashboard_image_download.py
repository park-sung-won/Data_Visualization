import tableauserverclient as TSC

TOKEN_NAME = 'test_token' #계정 혹은 token 발급
TOKEN_VALUE = 'test_token_value' 
SITE_NAME = 'wclub' # 태블로 프로젝트 폴더(?) 이름

tableau_auth = TSC.PersonalAccessTokenAuth(TOKEN_NAME, TOKEN_VALUE, SITE_NAME)

server_url = 'https://prod-apnortheast-a.online.tableau.com/' # 태블로 URL
server = TSC.Server( server_url , use_server_version=True)


with server.auth.sign_in(tableau_auth):
    for view in TSC.Pager(server.views):
        if '대시보드 2' in view.name:
            view_id = view.id
            view_data_by_id = server.views.get_by_id(view_id)
            print(view.name , view_id )

            with server.auth.sign_in(tableau_auth):
                server.views.populate_image(view_data_by_id)
                with open('저장경로/view_image.png', 'wb') as f:
                     f.write(view_data_by_id.image)

            # PDF 다운로드
            # server.views.populate_pdf(view_data_by_id, req_options=None)
            # with open('저장경로/view_image.pdf', 'wb') as f:
            #     f.write(view_data_by_id.pdf)
            

server.auth.sign_out()
