export default function getStudentIdsSum(students) {
  return students.reduce((acc, currentValue) => acc + currentValue.id, 0);
}
