# Frontend

## Stack
- React 19 with TypeScript
- Vite 8
- ESLint with react-hooks and react-refresh plugins
- Source lives in `frontend/src/`

## Running locally
```bash
cd frontend
npm run dev
```
Runs on `http://localhost:5173` by default.

## Building
```bash
cd frontend
npm run build
```
Runs `tsc -b` then `vite build`. Output goes to `frontend/dist/`.

## Linting
```bash
cd frontend
npm run lint
```
- ESLint with TypeScript support
- Always lint before committing

## Conventions
- Components go in `frontend/src/components/`
- Keep `App.tsx` as the top-level layout/router only — avoid business logic there
- Use TypeScript strictly — avoid `any`
- The Vite dev server proxies to the FastAPI backend at `http://localhost:8000` — configure `vite.config.ts` if you need to add proxy rules
- Do not change dependency versions without Engineering Lead approval
