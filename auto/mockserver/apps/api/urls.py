# coding=utf-8

from handlers import IndexHandler, LoginHandler, NewProjectHandler, ListAllProjectsHandler, NewModuleHandler, \
    GetProjectNameHandler, ListProjectModulesHandler, NewApiHandler, ListProjectApis, GetProjectDescHandler, \
    ListApisByMidHandler, GetApiDataHandler, SaveApiDataHandler, ListAllResponseTypesHandler, GetConsulEnvInfoHandler, \
    SaveConsulEnvInfoHandler,GetAuthInfoHandler,LogoutHandler
from tornado.web import url

urls = [
    url(r'', IndexHandler, name="index"),
    url(r'login', LoginHandler, name='login'),
    url(r'logout', LogoutHandler, name='logout'),
    url(r'getauthinfo', GetAuthInfoHandler, 'getauthinfo'),
    url(r'newProject', NewProjectHandler, name='newProject'),
    url(r'listAllProjects', ListAllProjectsHandler, name='listAllProjects'),
    url(r'newModule', NewModuleHandler, name='newModule'),
    url(r'getProjectName', GetProjectNameHandler, name='getProjectName'),
    url(r'listProjectModules', ListProjectModulesHandler, name='listProjectModules'),
    url(r'newApi', NewApiHandler, name='newApi'),
    url(r'listProjectApis', ListProjectApis, 'listProjectApis'),
    url(r'getProjectDesc', GetProjectDescHandler, 'getProjectDesc'),
    url(r'listApisByMid', ListApisByMidHandler, 'listApisByMid'),
    url(r'getApiData', GetApiDataHandler, 'getApiData'),
    url(r'saveApiData', SaveApiDataHandler, 'saveApiData'),
    url(r'listAllResponseTypes', ListAllResponseTypesHandler, 'listAllResponseTypes'),
    url(r'getConsulEnvInfo', GetConsulEnvInfoHandler, 'getConsulEnvInfo'),
    url(r'saveConsulEnvInfo', SaveConsulEnvInfoHandler, 'saveConsulEnvInfo'),
]
