from src.app import activities


def test_unregister_success_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"
    assert email in activities[activity_name]["participants"]

    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]


def test_unregister_returns_404_for_missing_activity(client):
    # Arrange
    activity_name = "Not A Real Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload["detail"] == "Activity not found"


def test_unregister_returns_400_when_student_not_signed_up(client):
    # Arrange
    activity_name = "Chess Club"
    email = "ghoststudent@mergington.edu"
    assert email not in activities[activity_name]["participants"]

    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 400
    assert payload["detail"] == "Student is not signed up for this activity"
