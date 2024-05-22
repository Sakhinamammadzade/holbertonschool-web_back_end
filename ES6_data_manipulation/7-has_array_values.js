export default function hasValuesFromArray(set, array) {
  const setSet = new Set(set);
  const arrSet = new Set(array);

  for (const elem of arrSet) {
    if (!setSet.has(elem)) {
      return false;
    }
  }
  return true;
}
