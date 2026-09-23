import { useState } from "react";
import { useSearchParams } from "react-router-dom";

const API_BASE = "http://127.0.0.1:8000";
const LOGIN_URL = "http://127.0.0.1:8000/accounts/login/"; // این رو با آدرس واقعی صفحه‌ی لاگینت جایگزین کن

export default function ResetPassword() {
  const [searchParams] = useSearchParams();
  const token = searchParams.get("token");

  const [password1, setPassword1] = useState("");
  const [password2, setPassword2] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setMessage("");
    setError("");

    try {
      const res = await fetch(
        `${API_BASE}/accounts/api/v1/password-reset-confirm/${token}/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            new_password1: password1,
            new_password2: password2,
          }),
        }
      );

      const data = await res.json();

      if (res.ok) {
        setMessage(data.detail);
      } else {
        setError(data.detail || JSON.stringify(data));
      }
    } catch (err) {
      setError("خطا در اتصال به سرور");
    } finally {
      setLoading(false);
    }
  };

  {/* Invalid token */}
  if (!token) {
    return (
      <div
        className="container content-space-3 content-space-t-lg-4"
        dir="rtl"
      >
        <div
          className="mx-auto"
          style={{
            maxWidth: "28rem",
          }}
        >
          <div className="alert alert-soft-danger text-center">
            لینک نامعتبر است — توکن یافت نشد.
          </div>
        </div>
      </div>
    );
  }

  return (
    <div
      className="container content-space-3 content-space-t-lg-4 content-space-b-lg-3"
      dir="rtl"
    >
      <div
        className="mx-auto"
        style={{
          maxWidth: "28rem",
        }}
      >
        {/* Card */}
        <div
          className="card"
          style={{
            border: "0.0625rem solid rgba(33, 50, 91, 0.1)",
            borderRadius: "0.75rem",
            boxShadow: "0 0.5rem 2rem rgba(33, 50, 91, 0.08)",
          }}
        >
          <div className="card-body p-4 p-md-5">

            {/* Header */}
            <div className="text-center mb-5">
              <div
                className="icon icon-lg icon-soft-primary icon-circle mx-auto mb-4"
              >
                <span className="fs-4">🔑</span>
              </div>

              <h1 className="h2 mb-2">
                تعیین رمز عبور جدید
              </h1>

              <p className="text-muted mb-0">
                رمز عبور جدید خود را وارد کنید.
              </p>
            </div>

            {/* Form */}
            {!message && (
              <form onSubmit={handleSubmit}>

                {/* Password */}
                <div className="mb-4">
                  <label
                    className="form-label fw-semibold"
                    htmlFor="password1"
                  >
                    رمز عبور جدید
                  </label>

                  <input
                    type="password"
                    className="form-control form-control-lg"
                    id="password1"
                    placeholder="حداقل ۸ کاراکتر"
                    value={password1}
                    onChange={(e) => setPassword1(e.target.value)}
                    dir="ltr"
                    required
                  />
                </div>

                {/* Confirm Password */}
                <div className="mb-4">
                  <label
                    className="form-label fw-semibold"
                    htmlFor="password2"
                  >
                    تکرار رمز عبور جدید
                  </label>

                  <input
                    type="password"
                    className="form-control form-control-lg"
                    id="password2"
                    placeholder="رمز عبور را دوباره وارد کنید"
                    value={password2}
                    onChange={(e) => setPassword2(e.target.value)}
                    dir="ltr"
                    required
                  />
                </div>

                {/* Submit */}
                <div className="d-grid mb-4">
                  <button
                    type="submit"
                    className="btn btn-primary btn-lg btn-transition"
                    disabled={loading}
                  >
                    {loading
                      ? "در حال تغییر..."
                      : "تغییر رمز عبور"}
                  </button>
                </div>

              </form>
            )}

            {/* Success */}
            {message && (
              <>
                <div className="alert alert-soft-success text-center">
                  {message}
                </div>

                <div className="d-grid mt-4">
                  <a
                    href={LOGIN_URL}
                    className="btn btn-primary btn-lg btn-transition"
                  >
                    بازگشت به صفحه ورود
                  </a>
                </div>
              </>
            )}

            {/* Error */}
            {error && (
              <div className="alert alert-soft-danger text-center">
                {error}
              </div>
            )}

          </div>
        </div>
      </div>
    </div>
  );
}