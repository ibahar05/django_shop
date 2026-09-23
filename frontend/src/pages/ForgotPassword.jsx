import { useState } from "react";

const API_BASE = "http://127.0.0.1:8000";

export default function ForgotPassword() {
  const [email, setEmail] = useState("");
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
        `${API_BASE}/accounts/api/v1/password-reset-link/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email }),
        }
      );

      const data = await res.json();

      if (res.ok) {
        setMessage(data.detail);
        setEmail("");
      } else {
        setError(data.detail || "خطایی رخ داد");
      }
    } catch (err) {
      setError("خطا در اتصال به سرور");
    } finally {
      setLoading(false);
    }
  };

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
                <span className="fs-4">🔐</span>
              </div>

              <h1 className="h2 mb-2">
                فراموشی رمز عبور
              </h1>

              <p className="text-muted mb-0">
                ایمیل خود را وارد کنید تا لینک بازیابی رمز عبور برایتان
                ارسال شود.
              </p>
            </div>

            {/* Form */}
            <form onSubmit={handleSubmit}>
              <div className="mb-4">
                <label
                  className="form-label fw-semibold"
                  htmlFor="resetEmail"
                >
                  ایمیل شما
                </label>

                <input
                  type="email"
                  className="form-control form-control-lg"
                  id="resetEmail"
                  placeholder="email@site.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  dir="ltr"
                  required
                />
              </div>

              <div className="d-grid mb-4">
                <button
                  type="submit"
                  className="btn btn-primary btn-lg btn-transition"
                  disabled={loading}
                >
                  {loading
                    ? "در حال ارسال..."
                    : "ارسال لینک بازیابی"}
                </button>
              </div>

              {/* Success */}
              {message && (
                <div className="alert alert-soft-success text-center mb-0">
                  {message}
                </div>
              )}

              {/* Error */}
              {error && (
                <div className="alert alert-soft-danger text-center mb-0">
                  {error}
                </div>
              )}
            </form>

          </div>
        </div>
      </div>
    </div>
  );
}