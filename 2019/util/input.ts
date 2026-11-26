import { readFileSync } from 'fs'

export const getRawInput = () => readFileSync(process.env.AOC_INPUT!, 'utf8')

export const getInput = () => getRawInput().trim()

export const getSplitInput = (delimiter = '\n') => getInput().split(delimiter)

export const getInputLines = () => getSplitInput().map(s => s.trim())
