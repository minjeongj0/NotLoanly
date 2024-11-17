#routers.py
#RESTful API의 엔드포인트를 정의


from flask import Blueprint, request, jsonify
from .services import chat_with_gpt
from app.models import User  # User 모델 가져오기
from . import db
from .models import User
main_routes = Blueprint("main_routes", __name__)

@main_routes.route("/api/hello", methods=["GET"])
def say_hello():
    return jsonify({"message": "Hello, Flask!"})

#대출하는거
#user테이블의 loan_amount, interest_rate를 업데이트 해주는 엔드포인트
@main_routes.route("/api/loan/apply", methods=["POST"])
def apply_loan():
    try:
        # 요청 데이터 가져오기
        data = request.json
        user_id = data.get("user_id")
        loan_amount = data.get("loan_amount")
        interest_rate = data.get("interest_rate")

        # 필수 값 체크
        if not user_id or loan_amount is None or interest_rate is None:
            return jsonify({
                "status": "error",
                "message": "user_id, loan_amount, and interest_rate are required."
            }), 400

        # 데이터베이스에서 사용자 찾기
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": f"User with id {user_id} not found."
            }), 404

        # 사용자 데이터 업데이트
        user.loan_amount = loan_amount
        user.interest_rate = interest_rate
        db.session.commit()  # 변경 사항 저장

        return jsonify({
            "status": "success",
            "message": "Loan details updated successfully.",
            "updated_user": user.to_dict()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500


@main_routes.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    user_list = [user.to_dict() for user in users]
    return jsonify(user_list)