import myConfig from '@jarsec/eslint-config';

export default [
  ...myConfig,
  { rules: { 'unicorn/filename-case': 'off' } },
];
