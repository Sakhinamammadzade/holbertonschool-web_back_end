export default function updateUniqueItems(newMap) {
  if (!(newMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  newMap.forEach((value, key) => {
    if (value === 1) {
      newMap.set(key, 100);
    }
  });
  return newMap;
}
