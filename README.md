# cloud.cloverky

> AI 멀티 에이전트 기반 **냉장고 재고 관리 + 개인화 레시피 서비스 — "프리지(Fridge)"**
> FastAPI 백엔드 · Next.js 프론트엔드 · Obsidian 기획 문서가 한 곳에 모인 학습/실험용 모노레포.

---

## 프로젝트 개요

본 저장소는 **단일 배포 서비스가 아니라, 한 도메인(프리지)을 중심으로 백엔드·프론트엔드·기획 문서가 공존하는 작업 공간**이다.

핵심 서비스 *프리지(Fridge)* 는 4인의 에이전트가 협업해 동작한다 — **Manager**(입고) → **Chef**(레시피 실행) → **Reviewer**(피드백) → **Shopper**(보충). 각 에이전트는 향후 한 파이썬 모듈로 구현된다.

본 저장소의 **AI 협업 사상**은 [`CURSOR.md`](./CURSOR.md), **운영 규약**은 [`.cursorrules`](./.cursorrules), **코드 위생**은 [`CLAUDE.md`](./CLAUDE.md) 참조.

---

## 디렉터리 구조

```
cloud.cloverky/
├── docs/                                # Obsidian vault (한국어 강의/기획 메모)
│   └── cloverky/프리지개발/
│       ├── 260506_fridge_project_plan.md   # 에이전트/파일 구성안
│       ├── 260506_fridge_simple.md          # 서비스 정의·가치
│       └── 260506_fridge_UI.md              # 초기 플러터플로우 화면 가이드
│
├── fridge/
│   ├── fresh.cloverky/                  # 백엔드 (Python · FastAPI)
│   │   ├── apps/
│   │   │   ├── main.py                  # FastAPI 엔트리포인트
│   │   │   └── fridge/app/
│   │   │       ├── manager.py           # 입고 — 영수증/사진 기반 재고 등록 (예정)
│   │   │       ├── chef.py              # 실행 — 임박 재료 기반 레시피 제안 (예정)
│   │   │       ├── reviewer.py          # 피드백 — 취향 수집 → Chef 보정 (예정)
│   │   │       └── shopper.py           # 보충 — 부족 재료 추출 → 외부 연동 (예정)
│   │   └── requirements.txt
│   │
│   └── fridge.cloverky/                 # 프론트엔드 (Next.js 16 · React 19 · shadcn/ui)
│       ├── app/page.tsx                 # 메인 페이지 (현재는 Titanic QA 프로토타입 잔여)
│       ├── components/ui/               # shadcn/ui 컴포넌트 세트
│       └── package.json
│
├── main/
│   ├── api.cloverky/                    # 예약 (빈 디렉터리)
│   └── www.cloverky/                    # 예약 (빈 디렉터리)
│
├── CURSOR.md                            # AI 협업 사상 (Why)
├── .cursorrules                         # AI 운영 규약 (How)
├── CLAUDE.md                            # 코드 수준 위생 (What not)
└── README.md                            # 본 파일
```

---

## 작명 컨벤션 — 프리지 크루

> 파일명 = 인물명. 역할 → 인물 매핑을 외우면 모듈을 보지 않고도 흐름을 그릴 수 있다.

위치: `fridge/fresh.cloverky/apps/fridge/app/`

| 인물 | 역할 | 핵심 기능 (계획) |
|---|---|---|
| **Manager** | 입고 관리자 | 영수증/사진 OCR → 재고·유통기한 자동 등록 |
| **Chef** | 실행 요리사 | 유통기한 임박 재료 중심 레시피 제안, 조리 가이드 |
| **Reviewer** | 피드백 평가사 | 사용자 취향 수집, Chef 추천 보정 |
| **Shopper** | 구매 보충원 | 부족 재료 추출, 쇼핑 앱(이커머스) 연동 |

키 프레이즈: **"매니저가 입고하고, 셰프가 만든다."** (Manager가 데이터 진입점, Chef가 사용자 가치 진입점)

자세한 정의는 [`docs/cloverky/프리지개발/260506_fridge_simple.md`](./docs/cloverky/%ED%94%84%EB%A6%AC%EC%A7%80%EA%B0%9C%EB%B0%9C/260506_fridge_simple.md) 참조.

---

## 기술 스택

### 백엔드 — `fridge/fresh.cloverky/`

코드에서 직접 확인된 사용 기술:

- **Python 3.13** *(`__pycache__` 기준 추정)*
- **FastAPI** — 웹 프레임워크
- **Uvicorn** — ASGI 서버 (`uvicorn[standard]`)
- **pandas** — 데이터 적재/집계
- **scikit-learn**, **joblib** — 모델 학습/직렬화 (`requirements.txt` 명시)

의존성은 `fridge/fresh.cloverky/requirements.txt`에 고정되어 있다.

### 프론트엔드 — `fridge/fridge.cloverky/`

- **Next.js 16** · **React 19** · **TypeScript 5.7**
- **Tailwind CSS 4** · **shadcn/ui** (Radix 기반 컴포넌트)
- **lucide-react**, **recharts**, **react-hook-form**, **zod**
- v0(Vercel)로 초기 스캐폴드된 프로젝트 (`fridge.cloverky/README.md` 참조)

---

## 셋업

### 1. 백엔드

```powershell
cd fridge\fresh.cloverky
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. 프론트엔드

```powershell
cd fridge\fridge.cloverky
pnpm install      # 또는 npm install
```

---

## 실행

### 백엔드 (FastAPI)

```powershell
cd fridge\fresh.cloverky\apps
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

- http://127.0.0.1:8000/docs — 자동 생성된 Swagger UI

> ⚠ 현재 `apps/main.py`는 미존재 모듈을 import 하므로 그대로 실행 시 실패한다. 아래 "알려진 이슈" 1번 참조.

### 프론트엔드 (Next.js)

```powershell
cd fridge\fridge.cloverky
pnpm dev          # 또는 npm run dev
```

- http://localhost:3000

환경 변수:

| 키 | 기본값 | 용도 |
|---|---|---|
| `NEXT_PUBLIC_API_BASE_URL` | `http://127.0.0.1:8000` | 프론트에서 호출할 백엔드 베이스 URL |

---

## AI 협업 규약

본 저장소는 AI 에이전트(Cursor 등) 협업을 전제로 한다. **세 파일이 하나의 하네스를 구성**한다.

| 파일 | 추상 수준 | 무엇을 담는가 |
|---|---|---|
| [`CURSOR.md`](./CURSOR.md) | Why | 협업의 사상·원칙 (변하지 않음) |
| [`.cursorrules`](./.cursorrules) | How | 에이전트 운영 규약 (매 작업에 적용) |
| [`CLAUDE.md`](./CLAUDE.md) | What not | 코드 수준 위생 (diff 제약) |

충돌 시 우선순위: **`CURSOR.md` > `.cursorrules` > `CLAUDE.md`** (사상 > 규약 > 위생).
새로운 기여자(사람이든 AI든)는 작업 전에 위 세 파일을 1회 통독한다.

---

## 알려진 이슈 (현재 코드 상태의 솔직한 보고)

> 본 README는 실제 코드 읽기로 작성됐다. 아래는 **확인된 문제**이며, README 정비 범위 밖이므로 *수정하지 않고 보고만* 한다.

1. **`fridge/fresh.cloverky/apps/main.py`의 import 깨짐**
   - `doro.app.doro_director`, `titanic.app.james_controller`를 import 하지만, 두 모듈은 현재 저장소에 존재하지 않는다 → 그대로 실행 시 `ImportError`.
   - 옛 학습 모듈(`doro`/`titanic`)의 잔여 코드로 보인다.

2. **`fridge/app/*.py`의 `IndentationError`** *(4개 파일 전부)*
   - `manager.py`, `chef.py`, `reviewer.py`, `shopper.py` 모두 `class X:` 다음 줄의 docstring이 **클래스 본문 밖** 들여쓰기로 작성되어 있다.
   - import 시 `IndentationError` 발생. docstring을 클래스/메서드 본문 안 들여쓰기로 옮겨야 한다.

3. **빈 `__init__.py`**
   - `fridge/fresh.cloverky/apps/fridge/__init__.py`, `.../fridge/app/__init__.py`가 0바이트 (정상 동작 가능).
   - 단, `apps/__init__.py`는 없으므로 모듈 경로는 `apps/`를 작업 디렉터리로 두고 실행해야 한다.

4. **프론트 `app/page.tsx`의 잔여 프로토타입**
   - v0가 만든 **Titanic QA UI**가 그대로 남아 있다 (`/titanic/qa`, `/titanic/data` 호출).
   - 실제 프리지(냉장고) 서비스 화면이 아니며, 향후 프리지 대시보드로 교체 예정.

5. **빈 예약 디렉터리** — `main/api.cloverky/`, `main/www.cloverky/`는 비어 있다.

6. **이름 규칙 혼재** — 루트는 `cloud.cloverky`, 백엔드는 `fresh.cloverky`, 프론트는 `fridge.cloverky`. 다음 정리 시 일관성 검토 필요.

---

## 로드맵 (요약)

- [ ] `fridge/app/*.py`의 들여쓰기 오류 정리 (docstring을 클래스 본문 안으로 이동)
- [ ] `apps/main.py`의 미존재 모듈 import 제거 또는 모듈 복구
- [ ] 4인 에이전트 간 데이터 흐름 설계 (Manager → Chef → Shopper, Reviewer 피드백 루프)
- [ ] 프론트 `app/page.tsx`를 프리지 대시보드(재고 게이지 + 레시피 카드 + 에이전트 상태바)로 교체
- [ ] 백엔드 ↔ 프론트 API 계약 문서화 (`docs/` 하위)
- [ ] `main/api.cloverky`, `main/www.cloverky` 용도 결정 또는 제거

---

## 데이터 / 외부 자원

- Obsidian vault: `docs/` (한국어 강의 메모 + 프리지 기획)
- 의존성 파일: `fridge/fresh.cloverky/requirements.txt`, `fridge/fridge.cloverky/package.json`

---

## 라이선스

미정 (TBD).
