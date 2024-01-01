export const chunk = (arr, size = 1) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (_, i) =>
    arr.slice(i * size, i * size + size)
  )

export const sortArray = (arr, asc = true) => {
  if (asc) {
    return arr.sort((a, b) => a - b)
  }

  return arr.sort((a, b) => b - a)
}

export const zip = (arrays) => {
  return Array.from({
    length: Math.max(...arrays.map(a => a.length)),
  }, (_, i) => arrays.map(a => a[i]))
}