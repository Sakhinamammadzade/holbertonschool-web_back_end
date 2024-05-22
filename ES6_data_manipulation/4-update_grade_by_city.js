export default function updateStudentGradeByCity(students, city, newGrades){
  return students
    .filter((student) => student.location === city)
    .map((student) => {
    const newGrade = newGrades.find((gradeObj) => gradeObj.studentId === student.id);
    return {
    ...student,
    grade: newGrade ? newGrade.grade: 'N/A'
    };
    });
}
