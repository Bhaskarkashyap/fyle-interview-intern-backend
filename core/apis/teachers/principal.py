from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from core.apis.teachers.schema import TeacherSchema

principal_assignments_resources_t = Blueprint('principal_assignments_resources_v1', __name__)

@principal_assignments_resources_t.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    teachers_list = Teacher.get_teachers_list()
    teachers_list_dump = TeacherSchema().dump(teachers_list, many=True)
    return APIResponse.respond(data = teachers_list_dump)